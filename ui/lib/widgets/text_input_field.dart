import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';

import '../model/login_model.dart';

class TextInputField extends StatelessWidget {
  final LoginModel model;
  final String textLable;
  final TextEditingController? controller;
  final FocusNode? focusNode;
  final TextInputType textInputType;
  final String? Function(String?)? validator;
  final String autofillHint;
  final Widget? suffixIcon;

  const TextInputField(
      {super.key,
      required this.model,
      required this.textLable,
      required this.controller,
      required this.focusNode,
      required this.textInputType,
      required this.validator,
      required this.autofillHint,
      this.suffixIcon});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsetsDirectional.fromSTEB(0, 0, 0, 16),
      child: SizedBox(
        width: double.infinity,
        child: TextFormField(
          controller: controller,
          focusNode: focusNode,
          autofocus: true,
          autofillHints: [autofillHint],
          obscureText: false,
          decoration: InputDecoration(
            labelText: textLable,
            labelStyle: FlutterFlowTheme.of(context).labelMedium.override(
                  fontFamily: 'Readex Pro',
                  letterSpacing: 0,
                ),
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: FlutterFlowTheme.of(context).secondaryBackground,
                width: 2,
              ),
              borderRadius: BorderRadius.circular(12),
            ),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: FlutterFlowTheme.of(context).primary,
                width: 2,
              ),
              borderRadius: BorderRadius.circular(12),
            ),
            errorBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: FlutterFlowTheme.of(context).error,
                width: 2,
              ),
              borderRadius: BorderRadius.circular(12),
            ),
            focusedErrorBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: FlutterFlowTheme.of(context).error,
                width: 2,
              ),
              borderRadius: BorderRadius.circular(12),
            ),
            filled: true,
            fillColor: FlutterFlowTheme.of(context).secondaryBackground,
            suffixIcon: suffixIcon,
          ),
          style: FlutterFlowTheme.of(context).bodyMedium.override(
                fontFamily: 'Readex Pro',
                letterSpacing: 0,
              ),
          minLines: null,
          keyboardType: textInputType,
          cursorColor: FlutterFlowTheme.of(context).primary,
          validator: validator,
          inputFormatters: [],
        ),
      ),
    );
  }
}
