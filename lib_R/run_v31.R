library("r2ddi")

dir2xml(
  path_in = "/home/soepdist/ddionrails/soep-core/v31/en/",
  path_out = "r2ddi/v31/en",
  missing_codes = -9:-1,
  my_cores = 30)

dir2xml(
  path_in = "/home/soepdist/ddionrails/soep-core/v31/de/",
  path_out = "r2ddi/v31/de/",
  missing_codes = -9:-1,
  my_cores = 30)
