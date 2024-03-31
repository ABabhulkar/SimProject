import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';

import '../pages/auth_3_verify_phone.dart' show Auth3VerifyPhoneWidget;

class Auth3VerifyPhoneModel extends FlutterFlowModel<Auth3VerifyPhoneWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  // State field(s) for PinCode widget.
  TextEditingController? pinCodeController;
  String? Function(BuildContext, String?)? pinCodeControllerValidator;

  @override
  void initState(BuildContext context) {
    pinCodeController = TextEditingController();
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    pinCodeController?.dispose();
  }
}
