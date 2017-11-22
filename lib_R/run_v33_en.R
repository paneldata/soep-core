library("r2ddi")

dir2xml(
  path_in = "/home/soepdist/ddionrails/soep-core/v33/en/",
  path_out = "r2ddi/v33/en",
  missing_codes = -9:-1,
  my_cores = 30)
