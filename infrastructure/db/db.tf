##########
# INPUTS #
##########
# *(string) TABLE_NAME
# *(list(string)) TEMP_OWNERS

# Create a table in the db
resource "aws_dynamodb_table" "dynamo_table" {
  name = var.TABLE_NAME
  billing_mode = "PROVISIONED"
  read_capacity= "20"
  write_capacity= "20"
  hash_key = "ID"

  attribute {
    name = "ID"
    type = "S"
  }
}

