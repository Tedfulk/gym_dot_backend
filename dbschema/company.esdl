module company {
    type Facilities {
        required property name -> str {
        constraint min_len_value(3);
        }
    }
    type Company {
        required property name -> str {
        constraint min_len_value(3);
        };
        multi link facility -> Facilities;
    };
}