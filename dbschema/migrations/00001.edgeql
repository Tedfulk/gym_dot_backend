CREATE MIGRATION m16dshr6tno7mssgt7qski4emyvbhri6lqpjwaacwd7wk7m4i5ni5q
    ONTO initial
{
  CREATE MODULE company IF NOT EXISTS;
  CREATE FUTURE nonrecursive_access_policies;
  CREATE TYPE company::Facilities {
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
  };
  CREATE TYPE company::Company {
      CREATE MULTI LINK facility -> company::Facilities;
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::min_len_value(3);
      };
  };
};
