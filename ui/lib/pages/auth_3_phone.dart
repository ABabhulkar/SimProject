import '/auth/firebase_auth/auth_util.dart';
import '/flutter_flow/flutter_flow_animations.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

import 'auth3_create_model.dart';
export 'auth3_create_model.dart';

class Auth3CreateWidget extends StatefulWidget {
  const Auth3CreateWidget({super.key});

  @override
  State<Auth3CreateWidget> createState() => _Auth3CreateWidgetState();
}

class _Auth3CreateWidgetState extends State<Auth3CreateWidget>
    with TickerProviderStateMixin {
  late Auth3CreateModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  final animationsMap = {
    'containerOnPageLoadAnimation': AnimationInfo(
      trigger: AnimationTrigger.onPageLoad,
      effects: [
        VisibilityEffect(duration: 1.ms),
        FadeEffect(
          curve: Curves.easeInOut,
          delay: 0.ms,
          duration: 400.ms,
          begin: 0,
          end: 1,
        ),
        ScaleEffect(
          curve: Curves.easeInOut,
          delay: 0.ms,
          duration: 400.ms,
          begin: Offset(0.9, 0.9),
          end: Offset(1, 1),
        ),
        TiltEffect(
          curve: Curves.easeInOut,
          delay: 0.ms,
          duration: 400.ms,
          begin: Offset(0, 0.524),
          end: Offset(0, 0),
        ),
      ],
    ),
  };

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => Auth3CreateModel());

    _model.emailAddressController ??= TextEditingController();
    _model.emailAddressFocusNode ??= FocusNode();

    _model.passwordController ??= TextEditingController();
    _model.passwordFocusNode ??= FocusNode();

    _model.passwordConfirmController ??= TextEditingController();
    _model.passwordConfirmFocusNode ??= FocusNode();
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => _model.unfocusNode.canRequestFocus
          ? FocusScope.of(context).requestFocus(_model.unfocusNode)
          : FocusScope.of(context).unfocus(),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
        body: SafeArea(
          top: true,
          child: Row(
            mainAxisSize: MainAxisSize.max,
            children: [
              if (responsiveVisibility(
                context: context,
                phone: false,
                tablet: false,
              ))
                Expanded(
                  flex: 5,
                  child: Align(
                    alignment: AlignmentDirectional(0, -1),
                    child: Container(
                      width: double.infinity,
                      height: double.infinity,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            FlutterFlowTheme.of(context).primaryBackground,
                            FlutterFlowTheme.of(context).primary
                          ],
                          stops: [0, 1],
                          begin: AlignmentDirectional(1, 0),
                          end: AlignmentDirectional(-1, 0),
                        ),
                        borderRadius: BorderRadius.circular(0),
                      ),
                    ),
                  ),
                ),
              Expanded(
                flex: 5,
                child: Align(
                  alignment: AlignmentDirectional(0, 0),
                  child: Padding(
                    padding: EdgeInsets.all(16),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(16),
                      child: Container(
                        width: double.infinity,
                        height: double.infinity,
                        constraints: BoxConstraints(
                          maxWidth: 570,
                        ),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(16),
                        ),
                        alignment: AlignmentDirectional(0, -1),
                        child: SingleChildScrollView(
                          child: Column(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                width: double.infinity,
                                height: 140,
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.only(
                                    bottomLeft: Radius.circular(16),
                                    bottomRight: Radius.circular(16),
                                    topLeft: Radius.circular(0),
                                    topRight: Radius.circular(0),
                                  ),
                                ),
                                alignment: AlignmentDirectional(-1, 0),
                                child: Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      16, 0, 16, 0),
                                  child: Row(
                                    mainAxisSize: MainAxisSize.max,
                                    mainAxisAlignment: MainAxisAlignment.start,
                                    children: [
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 0, 12, 0),
                                        child: Icon(
                                          Icons.flourescent_rounded,
                                          color: FlutterFlowTheme.of(context)
                                              .primary,
                                          size: 44,
                                        ),
                                      ),
                                      Text(
                                        'SimProject',
                                        style: FlutterFlowTheme.of(context)
                                            .displaySmall
                                            .override(
                                          fontFamily: 'Outfit',
                                          letterSpacing: 0,
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Align(
                                alignment: AlignmentDirectional(0, 0),
                                child: Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      16, 0, 16, 32),
                                  child: Column(
                                    mainAxisSize: MainAxisSize.max,
                                    crossAxisAlignment:
                                    CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        'Create an account',
                                        style: FlutterFlowTheme.of(context)
                                            .displaySmall
                                            .override(
                                          fontFamily: 'Outfit',
                                          letterSpacing: 0,
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 4, 0, 24),
                                        child: Text(
                                          'Let\'s get started by filling out the form below.',
                                          style: FlutterFlowTheme.of(context)
                                              .labelLarge
                                              .override(
                                            fontFamily: 'Readex Pro',
                                            letterSpacing: 0,
                                          ),
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 0, 0, 16),
                                        child: Container(
                                          width: double.infinity,
                                          child: TextFormField(
                                            controller:
                                            _model.emailAddressController,
                                            focusNode:
                                            _model.emailAddressFocusNode,
                                            autofocus: true,
                                            autofillHints: [
                                              AutofillHints.email
                                            ],
                                            obscureText: false,
                                            decoration: InputDecoration(
                                              labelText: 'Email',
                                              labelStyle:
                                              FlutterFlowTheme.of(context)
                                                  .labelMedium
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                              enabledBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .secondaryBackground,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .primary,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              errorBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedErrorBorder:
                                              OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              filled: true,
                                              fillColor:
                                              FlutterFlowTheme.of(context)
                                                  .secondaryBackground,
                                            ),
                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                              fontFamily: 'Readex Pro',
                                              letterSpacing: 0,
                                            ),
                                            minLines: null,
                                            keyboardType:
                                            TextInputType.emailAddress,
                                            cursorColor:
                                            FlutterFlowTheme.of(context)
                                                .primary,
                                            validator: _model
                                                .emailAddressControllerValidator
                                                .asValidator(context),
                                          ),
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 0, 0, 16),
                                        child: Container(
                                          width: double.infinity,
                                          child: TextFormField(
                                            controller:
                                            _model.passwordController,
                                            focusNode: _model.passwordFocusNode,
                                            autofocus: true,
                                            autofillHints: [
                                              AutofillHints.password
                                            ],
                                            obscureText:
                                            !_model.passwordVisibility,
                                            decoration: InputDecoration(
                                              labelText: 'Password',
                                              labelStyle:
                                              FlutterFlowTheme.of(context)
                                                  .labelMedium
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                              enabledBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .secondaryBackground,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .primary,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              errorBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedErrorBorder:
                                              OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              filled: true,
                                              fillColor:
                                              FlutterFlowTheme.of(context)
                                                  .secondaryBackground,
                                              suffixIcon: InkWell(
                                                onTap: () => setState(
                                                      () => _model
                                                      .passwordVisibility =
                                                  !_model
                                                      .passwordVisibility,
                                                ),
                                                focusNode: FocusNode(
                                                    skipTraversal: true),
                                                child: Icon(
                                                  _model.passwordVisibility
                                                      ? Icons
                                                      .visibility_outlined
                                                      : Icons
                                                      .visibility_off_outlined,
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .secondaryText,
                                                  size: 24,
                                                ),
                                              ),
                                            ),
                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                              fontFamily: 'Readex Pro',
                                              letterSpacing: 0,
                                            ),
                                            minLines: null,
                                            cursorColor:
                                            FlutterFlowTheme.of(context)
                                                .primary,
                                            validator: _model
                                                .passwordControllerValidator
                                                .asValidator(context),
                                          ),
                                        ),
                                      ),
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 0, 0, 16),
                                        child: Container(
                                          width: double.infinity,
                                          child: TextFormField(
                                            controller: _model
                                                .passwordConfirmController,
                                            focusNode:
                                            _model.passwordConfirmFocusNode,
                                            autofocus: true,
                                            autofillHints: [
                                              AutofillHints.password
                                            ],
                                            obscureText: !_model
                                                .passwordConfirmVisibility,
                                            decoration: InputDecoration(
                                              labelText: 'Confirm Password',
                                              labelStyle:
                                              FlutterFlowTheme.of(context)
                                                  .labelMedium
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                              enabledBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .secondaryBackground,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .primary,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              errorBorder: OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              focusedErrorBorder:
                                              OutlineInputBorder(
                                                borderSide: BorderSide(
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .error,
                                                  width: 2,
                                                ),
                                                borderRadius:
                                                BorderRadius.circular(12),
                                              ),
                                              filled: true,
                                              fillColor:
                                              FlutterFlowTheme.of(context)
                                                  .secondaryBackground,
                                              suffixIcon: InkWell(
                                                onTap: () => setState(
                                                      () => _model
                                                      .passwordConfirmVisibility =
                                                  !_model
                                                      .passwordConfirmVisibility,
                                                ),
                                                focusNode: FocusNode(
                                                    skipTraversal: true),
                                                child: Icon(
                                                  _model.passwordConfirmVisibility
                                                      ? Icons
                                                      .visibility_outlined
                                                      : Icons
                                                      .visibility_off_outlined,
                                                  color: FlutterFlowTheme.of(
                                                      context)
                                                      .secondaryText,
                                                  size: 24,
                                                ),
                                              ),
                                            ),
                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                              fontFamily: 'Readex Pro',
                                              letterSpacing: 0,
                                            ),
                                            cursorColor:
                                            FlutterFlowTheme.of(context)
                                                .primary,
                                            validator: _model
                                                .passwordConfirmControllerValidator
                                                .asValidator(context),
                                          ),
                                        ),
                                      ),
                                      Align(
                                        alignment: AlignmentDirectional(1, -1),
                                        child: Padding(
                                          padding:
                                          EdgeInsetsDirectional.fromSTEB(
                                              0, 0, 0, 16),
                                          child: FFButtonWidget(
                                            onPressed: () async {
                                              GoRouter.of(context)
                                                  .prepareAuthEvent();
                                              if (_model.passwordController
                                                  .text !=
                                                  _model
                                                      .passwordConfirmController
                                                      .text) {
                                                ScaffoldMessenger.of(context)
                                                    .showSnackBar(
                                                  SnackBar(
                                                    content: Text(
                                                      'Passwords don\'t match!',
                                                    ),
                                                  ),
                                                );
                                                return;
                                              }

                                              final user = await authManager
                                                  .createAccountWithEmail(
                                                context,
                                                _model.emailAddressController
                                                    .text,
                                                _model.passwordController.text,
                                              );
                                              if (user == null) {
                                                return;
                                              }

                                              context.goNamedAuth(
                                                  'HomePage', context.mounted);
                                            },
                                            text: 'Create Account',
                                            options: FFButtonOptions(
                                              width: 200,
                                              height: 44,
                                              padding: EdgeInsetsDirectional
                                                  .fromSTEB(0, 0, 0, 0),
                                              iconPadding: EdgeInsetsDirectional
                                                  .fromSTEB(0, 0, 0, 0),
                                              color:
                                              FlutterFlowTheme.of(context)
                                                  .primary,
                                              textStyle:
                                              FlutterFlowTheme.of(context)
                                                  .titleSmall
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                color: Colors.white,
                                                letterSpacing: 0,
                                              ),
                                              elevation: 3,
                                              borderSide: BorderSide(
                                                color: Colors.transparent,
                                                width: 1,
                                              ),
                                              borderRadius:
                                              BorderRadius.circular(12),
                                            ),
                                          ),
                                        ),
                                      ),

                                      // You will have to add an action on this rich text to go to your login page.
                                      Padding(
                                        padding: EdgeInsetsDirectional.fromSTEB(
                                            0, 12, 0, 12),
                                        child: InkWell(
                                          splashColor: Colors.transparent,
                                          focusColor: Colors.transparent,
                                          hoverColor: Colors.transparent,
                                          highlightColor: Colors.transparent,
                                          onTap: () async {
                                            context.pushNamed(
                                              'auth_3_Login',
                                              extra: <String, dynamic>{
                                                kTransitionInfoKey:
                                                TransitionInfo(
                                                  hasTransition: true,
                                                  transitionType:
                                                  PageTransitionType.fade,
                                                  duration:
                                                  Duration(milliseconds: 0),
                                                ),
                                              },
                                            );
                                          },
                                          child: RichText(
                                            textScaler: MediaQuery.of(context)
                                                .textScaler,
                                            text: TextSpan(
                                              children: [
                                                TextSpan(
                                                  text:
                                                  'Already have an account? ',
                                                  style: TextStyle(),
                                                ),
                                                TextSpan(
                                                  text: 'Sign In here',
                                                  style: FlutterFlowTheme.of(
                                                      context)
                                                      .bodyMedium
                                                      .override(
                                                    fontFamily:
                                                    'Readex Pro',
                                                    color:
                                                    FlutterFlowTheme.of(
                                                        context)
                                                        .primary,
                                                    fontSize: 16,
                                                    letterSpacing: 0,
                                                    fontWeight:
                                                    FontWeight.w600,
                                                  ),
                                                )
                                              ],
                                              style:
                                              FlutterFlowTheme.of(context)
                                                  .labelLarge
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                            ),
                                          ),
                                        ),
                                      ),
                                      Divider(
                                        height: 20,
                                        thickness: 1,
                                        color: FlutterFlowTheme.of(context)
                                            .alternate,
                                      ),

                                      // You will have to add an action on this rich text to go to your login page.
                                      if (responsiveVisibility(
                                        context: context,
                                        desktop: false,
                                      ))
                                        Padding(
                                          padding:
                                          EdgeInsetsDirectional.fromSTEB(
                                              0, 12, 0, 12),
                                          child: RichText(
                                            textScaler: MediaQuery.of(context)
                                                .textScaler,
                                            text: TextSpan(
                                              children: [
                                                TextSpan(
                                                  text: 'Additional options:',
                                                  style: TextStyle(),
                                                )
                                              ],
                                              style:
                                              FlutterFlowTheme.of(context)
                                                  .labelLarge
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                            ),
                                          ),
                                        ),
                                      if (responsiveVisibility(
                                        context: context,
                                        desktop: false,
                                      ))
                                        Align(
                                          alignment:
                                          AlignmentDirectional(-1, -1),
                                          child: FFButtonWidget(
                                            onPressed: () async {
                                              context.pushNamed(
                                                'auth_3_phone',
                                                extra: <String, dynamic>{
                                                  kTransitionInfoKey:
                                                  TransitionInfo(
                                                    hasTransition: true,
                                                    transitionType:
                                                    PageTransitionType.fade,
                                                    duration: Duration(
                                                        milliseconds: 0),
                                                  ),
                                                },
                                              );
                                            },
                                            text: 'Continue with Phone',
                                            icon: Icon(
                                              Icons.phone_sharp,
                                              size: 15,
                                            ),
                                            options: FFButtonOptions(
                                              width: double.infinity,
                                              height: 44,
                                              padding: EdgeInsetsDirectional
                                                  .fromSTEB(24, 0, 24, 0),
                                              iconPadding: EdgeInsetsDirectional
                                                  .fromSTEB(0, 0, 0, 0),
                                              color:
                                              FlutterFlowTheme.of(context)
                                                  .primaryBackground,
                                              textStyle:
                                              FlutterFlowTheme.of(context)
                                                  .bodyMedium
                                                  .override(
                                                fontFamily:
                                                'Readex Pro',
                                                letterSpacing: 0,
                                              ),
                                              elevation: 0,
                                              borderSide: BorderSide(
                                                color:
                                                FlutterFlowTheme.of(context)
                                                    .alternate,
                                                width: 2,
                                              ),
                                              borderRadius:
                                              BorderRadius.circular(12),
                                              hoverColor:
                                              FlutterFlowTheme.of(context)
                                                  .alternate,
                                              hoverBorderSide: BorderSide(
                                                color:
                                                FlutterFlowTheme.of(context)
                                                    .alternate,
                                                width: 2,
                                              ),
                                              hoverTextColor:
                                              FlutterFlowTheme.of(context)
                                                  .primaryText,
                                              hoverElevation: 3,
                                            ),
                                          ),
                                        ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ).animateOnPageLoad(
                        animationsMap['containerOnPageLoadAnimation']!),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
