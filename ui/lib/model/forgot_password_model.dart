import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

import '../pages/forgot_password_page.dart' show ForgotPasswordPageWidget;

class ForgotPasswordModel
    extends FlutterFlowModel<ForgotPasswordPageWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  // State field(s) for email widget.
  FocusNode? emailFocusNode;
  TextEditingController? emailController;
  final emailMask = MaskTextInputFormatter(mask: '(###) ###-####');
  String? Function(BuildContext, String?)? emailControllerValidator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    emailFocusNode?.dispose();
    emailController?.dispose();
  }
}
