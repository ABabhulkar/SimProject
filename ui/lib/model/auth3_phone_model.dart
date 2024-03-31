import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

import '../pages/auth_3_phone.dart' show Auth3PhoneWidget;

class Auth3PhoneModel extends FlutterFlowModel<Auth3PhoneWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  // State field(s) for phoneNumber widget.
  FocusNode? phoneNumberFocusNode;
  TextEditingController? phoneNumberController;
  final phoneNumberMask = MaskTextInputFormatter(mask: '(###) ###-####');
  String? Function(BuildContext, String?)? phoneNumberControllerValidator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
    phoneNumberFocusNode?.dispose();
    phoneNumberController?.dispose();
  }
}
