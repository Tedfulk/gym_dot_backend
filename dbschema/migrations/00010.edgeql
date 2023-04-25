CREATE MIGRATION m1gxbzkeuygvolscmi4sdwj3jnvh6tsqls44np6xaaa3nvnmlivona
    ONTO m1b4l42aqf4msrw57xgp3temvq2oh3ew3papcwewaegeo5alniriua
{
  ALTER TYPE default::Companies {
      ALTER LINK facility {
          ON TARGET DELETE ALLOW;
      };
  };
};
