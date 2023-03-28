CREATE MIGRATION m1vx2j4yqcuwbki7oszftjbsykw7musn2jxx63aamvupnhawdd5yca
    ONTO initial
{
  CREATE MODULE company IF NOT EXISTS;
  CREATE FUTURE nonrecursive_access_policies;
  CREATE TYPE company::Facilities {
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
  CREATE TYPE company::Company {
      CREATE MULTI LINK facility -> company::Facilities {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
  };
};
