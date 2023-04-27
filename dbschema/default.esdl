module default {
    type Companies {
        required property name -> str {
        constraint min_len_value(3);
        };
        multi link facility -> Facilities {
            constraint exclusive;
            on target delete allow;
        };
    };

    type Facilities {
        required property name -> str {
        constraint min_len_value(3);
        }
        property address -> str {
        constraint min_len_value(3);
        }
        property city -> str {
        constraint min_len_value(3);
        }
        property state -> str {
        constraint max_len_value(2);
        }
        multi link program -> Programs {
            constraint exclusive;
        };
    }

    type Programs {
        required property name -> str ;
        property description -> str ;
        property active -> bool {
            default := True;
        };
        multi link lesson -> Lessons {
            constraint exclusive;
        };
    }

    type Lessons {
        property class_dates -> array<cal::local_date>;
        property class_times -> array<cal::local_time>;
        property len_of_class_time -> int32 {
            default := 60
        };
        property active -> bool {
            default := True;
        };
        property max_attendees -> int32 {
            constraint min_value(1);
        };
        property min_attendees -> int32 {
            constraint min_value(1);
        };
        property waitlist -> int32 {
            default := 10;
        };
    }

    type Users {
        required property email -> str { constraint exclusive; };
        property first_name -> str;
        property last_name -> str;
        required property password_hash -> str ;
        property avatar_src -> str;
        property full_name := .first_name ++ ' ' ++ .last_name;
        property role -> Role {
            default := 'user';
        }
        multi link oauth_accounts -> OAuthUsers {
                # ensures a one-to-many relationship
                constraint exclusive;
                # Deleting this Object (User) will unconditionally delete
                # linked objects (oauth)
                on source delete delete target;
            }
        multi link access_token -> AccessToken {
            # ensures a one-to-many relationship
            constraint exclusive;
            # Deleting this Object (User) will unconditionally delete
            # linked objects (access)
            on source delete delete target;
        }
    }

    scalar type Role extending enum <"admin", "user">;

    type OAuthUsers {
        required property account_email -> str {
            constraint exclusive;
        }
        required property oauth_name -> str;
        required property account_id -> str;
        required property access_token -> str;
        property expires_at -> int32;
        property refresh_token -> str;

    }

    type AccessToken {
        required property token -> str {
            constraint exclusive;
        }
        required property created_at -> datetime {
            default := (datetime_current());
        };
    }
}
