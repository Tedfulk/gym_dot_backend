CREATE MIGRATION m14irvyyom3dfijlta3nlkmbydptlfmd3xvihtfzxqwhelsj4ciyya
    ONTO initial
{
  CREATE FUTURE nonrecursive_access_policies;
  CREATE TYPE default::Facilities {
      CREATE PROPERTY address -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
      CREATE PROPERTY city -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
      CREATE PROPERTY state -> std::str {
          CREATE CONSTRAINT std::max_len_value(2);
      };
  };
  CREATE TYPE default::Company {
      CREATE MULTI LINK facility -> default::Facilities {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
  };
};
