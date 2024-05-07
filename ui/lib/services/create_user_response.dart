class CreateUserResponse {
  int? userId;
  final String error;
  String token;

  CreateUserResponse(
      {this.userId, required this.error, this.token=''});

  factory CreateUserResponse.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {'user_id': int userId, 'error': String error, 'token': String token} =>
        CreateUserResponse(userId: userId, error: error, token: token),
      _ => throw const FormatException('Failed to load CreateUserResponse.'),
    };
  }
}
