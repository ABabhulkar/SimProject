import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';

import '../pages/create_user_page.dart' show CreateUserPageWidget;
import '../utils/utils.dart';

class CreateUserModel extends FlutterFlowModel<CreateUserPageWidget> {
  ///  State fields for stateful widgets in this page.
  final unfocusNode = FocusNode();

  // State field(s) for userName widget.
  FocusNode? userNameFocusNode;
  TextEditingController? userNameController;
  String? Function(BuildContext, String?)? userNameControllerValidator;

  // State field(s) for emailAddress widget.
  FocusNode? emailAddressFocusNode;
  TextEditingController? emailAddressController;
  String? Function(BuildContext, String?)? emailAddressControllerValidator;

  // State field(s) for password widget.
  FocusNode? passwordFocusNode;
  TextEditingController? passwordController;
  late bool passwordVisibility;
  String? Function(BuildContext, String?)? passwordControllerValidator;

  // State field(s) for passwordConfirm widget.
  FocusNode? passwordConfirmFocusNode;
  TextEditingController? passwordConfirmController;
  late bool passwordConfirmVisibility;
  String? Function(BuildContext, String?)? passwordConfirmControllerValidator;

  @override
  void initState(BuildContext context) {
    passwordVisibility = false;
    passwordConfirmVisibility = false;
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    userNameFocusNode?.dispose();
    userNameController?.dispose();
    emailAddressFocusNode?.dispose();
    emailAddressController?.dispose();

    passwordFocusNode?.dispose();
    passwordController?.dispose();

    passwordConfirmFocusNode?.dispose();
    passwordConfirmController?.dispose();
  }

  Map<String, dynamic> getValidatedData() {
    //TODO: Also add minimum size on password
    if(passwordConfirmController.text != passwordController.text){
      return {
        'error': 'Incorrect password'
      };
    }
    if(!Utils.isValidEmail(emailAddressController.text)){
      return {
        'error': 'Incorrect email'
      };
    }
    return {
      'error': 'Success',
      'username': userNameController.text,
      "email": emailAddressController.text,
      "password": passwordController.text,
      "metadata": {},
      "role": "user"
    };
  }
}
