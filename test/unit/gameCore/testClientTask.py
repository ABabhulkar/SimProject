import subprocess
import unittest
from unittest.mock import patch

from src.backend.gameCore.gameCore import ClientTask


class TestClientTask(unittest.TestCase):

    def test_init_sets_attributes(self):
        client = ClientTask(
            index=1, path="/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1")
        self.assertEqual(client.name, "P1")
        self.assertEqual(
            client.path, "/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1")
        self.assertIsNone(client.socket)
        self.assertFalse(client.startHandler)

    @patch("subprocess.Popen")
    def test_startApp_starts_process(self, mock_popen):
        logger = unittest.mock.Mock()
        client = ClientTask(
            index=1, path="/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1")
        client.startApp(logger)
        mock_popen.assert_called_with(
            ['/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1', 'P1'], stdout=subprocess.PIPE)
        logger.debug.assert_called_with(
            "command: ['/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1', 'P1']")

    @patch("os.path.isfile")
    def test_startApp_handles_missing_path(self, mock_isfile):
        logger = unittest.mock.Mock()
        mock_isfile.return_value = False
        client = ClientTask(index=1, path="/path/to/missing_app")
        client.startApp(logger)
        logger.info.assert_called_with("Folder path does not exist.")

    @patch("socket.socket.sendall")
    def test_sendCommand_sends_data(self, mock_sendall):
        socket = unittest.mock.MagicMock()
        client = ClientTask(
            index=1, path="/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1")
        client.socket = socket
        client.sendCommand("test command")
        mock_sendall.assert_called_with("test command".encode())

    @patch("socket.socket.sendall")
    def test_sendCommand_handles_socket_error(self, mock_sendall):
        socket = unittest.mock.MagicMock()
        socket.sendall.side_effect = OSError("Socket error")
        client = ClientTask(
            index=1, path="/mnt/d/Projects/PythonWS/SimProject/test/resources/TestApp1")
        client.socket = socket
        with self.assertRaises(OSError):
            client.sendCommand("test command")

    def test_parse_msg_connected_message(self):
        message = "P1:connected"
        value, is_ack = ClientTask.parse_msg(message)
        self.assertEqual(value, "P1")
        self.assertTrue(is_ack)

    def test_parse_msg_move_message(self):
        message = "P2:rock"
        value, is_ack = ClientTask.parse_msg(message)
        self.assertEqual(value, "rock")
        self.assertFalse(is_ack)

    def test_parse_msg_invalid_message(self):
        message = "invalid message"
        value, is_ack = ClientTask.parse_msg(message)
        self.assertIsNone(value)
        self.assertIsNone(is_ack)


if __name__ == '__main__':
    unittest.main(verbosity=2)
