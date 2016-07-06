
require 'csv'

csv_path = "import/soep-core"

logical_variables_sql = ["INSERT INTO logical_variables (study,logical_dataset,logical_variable,concept) VALUES\n"]

dataset_names = []

lv_temp = {}

CSV.foreach(File.join(csv_path, "logical_variables.csv"), headers: true) do |row|
  row = row.to_hash
  lv_temp["('#{row["study"]}','#{row["dataset"]}','#{row["variable"]}"] =
    "('#{row["study"]}','#{row["dataset"]}','#{row["variable"]}','#{row["concept"]}'),\n"
  dataset_names << row["dataset"]
end

lv_temp.each do |key, value|
  logical_variables_sql << value
end

logical_variables_sql = logical_variables_sql.uniq.join
logical_variables_sql = logical_variables_sql[0..-3]
logical_variables_sql << ";"

File.write("sql/logical_variables.sql", logical_variables_sql)

logical_datasets_sql = ["INSERT INTO logical_datasets (study,logical_dataset) VALUES"]

dataset_names.uniq.each do |dataset_name|
  logical_datasets_sql << "('soep-core','#{dataset_name}'),\n"

end

logical_datasets_sql = logical_datasets_sql.uniq.join
logical_datasets_sql = logical_datasets_sql[0..-3]
logical_datasets_sql << ";"

File.write "sql/logical_datasets.sql", logical_datasets_sql
