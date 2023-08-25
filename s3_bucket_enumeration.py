import boto3

def enumerate_s3_buckets(target_domain):
  """
  Enumerates all S3 buckets for a given domain.

  Args:
    target_domain: The domain name to enumerate.

  Returns:
    A list of all S3 buckets for the given domain.
  """

  s3 = boto3.client('s3')

  buckets = []

  for bucket_name in s3.list_buckets()['Buckets']:
    if target_domain in bucket_name['Name']:
      buckets.append(bucket_name['Name'])

  return buckets

def main():
  """
  The main function.
  """

  target_domain = input('Enter the domain name to enumerate: ')

  buckets = enumerate_s3_buckets(target_domain)

  print('The following S3 buckets [🪣] found for the Domain: {}'.format(target_domain))
  for bucket in buckets:
    print(bucket)

if __name__ == '__main__':
  main()
