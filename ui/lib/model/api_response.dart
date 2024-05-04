class APIResponse {
  final int code;
  final String message;
  final String token;

  const APIResponse({required this.code, required this.message, required this.token});

  factory APIResponse.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {'code': int code, 'message': String message,'token': String token} =>
        APIResponse(code: code, message: message, token: token),
      _ => throw const FormatException('Failed to load APIResponse.'),
    };
  }
}
