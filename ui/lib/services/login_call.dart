import 'package:flutter/foundation.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'package:intl/intl.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../model/api_response.dart';

class LoginCall {
  final String username;
  final String password;

  LoginCall({required this.username, required this.password});

  Future<APIResponse> call() async {
    try {
      // make the request
      Response response = await post(Uri.parse('http://127.0.0.1:5000/auth'),
          headers: <String, String>{
            'Content-Type': 'application/json',
          },
          body: jsonEncode(
              <String, String>{'username': username, 'password': password}));

      if (response.statusCode == 200) {
        // If the server did return a 200 OK response,
        // then parse the JSON.
        // Store access token securely using SharedPreferences
        final apiResponse = APIResponse.fromJson(
            jsonDecode(response.body) as Map<String, dynamic>);

        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('accessToken', apiResponse.token);
        return apiResponse;
      } else {
        // If the server did not return a 200 OK response,
        // then throw an exception.
        return APIResponse(
            code: response.statusCode, message: 'Server error', token: '');
      }
    } catch (e) {
      if (kDebugMode) {
        print(e);
      }
      return const APIResponse(code: 98, message: 'API call failed', token: '');
    }
  }
}
