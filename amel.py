class User:
    def _init_(self, user_id, username, password, email, user_preferences):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.user_preferences = user_preferences
    
    def get_user_preferences(self):
        return self.user_preferences

    def set_user_preferences(self, preferences):
        self.user_preferences = preferences
        print(f"User preferences updated: {preferences}")

    def register(self):
        print(f"User registered: {self.username}")

    def login(self, username, password):
        print(f"User logged in: {username}")
        return True

    def update_preferences(self, preferences):
        self.user_preferences = preferences
        print(f"Preferences updated: {preferences}")