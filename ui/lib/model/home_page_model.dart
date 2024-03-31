import 'package:flutter/material.dart';
import 'package:flutterflow_ui/flutterflow_ui.dart';

import '../components/home.dart';
import '../pages/home_page.dart' show HomePageWidget;

class HomePageModel extends FlutterFlowModel<HomePageWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  // State field(s) for TabBar widget.
  TabController? tabBarController;

  int get tabBarCurrentIndex =>
      tabBarController != null ? tabBarController!.index : 0;

  // Model for home component.
  late HomeModel homeModel;

  @override
  void initState(BuildContext context) {
    homeModel = createModel(context, () => HomeModel());
  }

  @override
  void dispose() {
    unfocusNode.dispose();
    tabBarController?.dispose();
    homeModel.dispose();
  }
}
