module company {
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

    }
    type Company {
        required property name -> str {
        constraint min_len_value(3);
        };
        multi link facility -> Facilities {
            constraint exclusive;
        };
    };
}