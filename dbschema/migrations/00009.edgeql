CREATE MIGRATION m1b4l42aqf4msrw57xgp3temvq2oh3ew3papcwewaegeo5alniriua
    ONTO m1onfapq5ylz5lc4dhlvy6c6hibnsw6r4uf5h7lmcppptufh6m4gpq
{
  ALTER TYPE default::Classes RENAME TO default::Lessons;
  ALTER TYPE default::Programs {
      ALTER LINK class {
          RENAME TO lesson;
      };
  };
};
