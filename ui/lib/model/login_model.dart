import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';

import '../pages/login_page.dart' show LoginPageWidget;

class LoginModel extends FlutterFlowModel<LoginPageWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  // State field(s) for emailAddress widget.
  FocusNode? userNameFocusNode;
  TextEditingController? userNameController;
  String? Function(BuildContext, String?)? userNameControllerValidator;

  // State field(s) for password widget.
  FocusNode? passwordFocusNode;
  TextEditingController? passwordController;
  late bool passwordVisibility;
  String? Function(BuildContext, String?)? passwordControllerValidator;

  @override
  void initState(BuildContext context) {
    passwordVisibility = false;
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    userNameFocusNode?.dispose();
    userNameController?.dispose();

    passwordFocusNode?.dispose();
    passwordController?.dispose();
  }
}
