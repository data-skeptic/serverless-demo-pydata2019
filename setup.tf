provider "aws" {
  region = "us-east-2"
}

resource "aws_dynamodb_table" "shout-outs" {
  name           = "ShoutOuts"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "name"

  attribute {
    name = "name"
    type = "S"
  }



  ttl {
    attribute_name = "ttl"
    enabled        = true
  }

}