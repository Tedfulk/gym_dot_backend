module default {
    type Companies {
        required property name -> str {
        constraint min_len_value(3);
        };
        multi link facility -> Facilities {
            constraint exclusive;
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
}
