SERVICE_ROLE_ARN = 'ServiceRoleArn'
LAMBDA_BASIC_EXECUTION_ROLE = 'AWSLambdaBasicExecutionRole'
SERVICE_ROLE = 'ServiceRole'
CREATE_LAMBDA = 'CreateOrder'
TABLE_NAME = 'orders'
IDEMPOTENCY_TABLE_NAME = 'IdempotencyTable'
TABLE_NAME_OUTPUT = 'DbOutput'
IDEMPOTENCY_TABLE_NAME_OUTPUT = 'IdempotencyDbOutput'
APIGATEWAY = 'Apigateway'
MONITORING_TOPIC = 'MonitoringTopic'
GW_RESOURCE = 'orders'
LAMBDA_LAYER_NAME = 'common'
API_HANDLER_LAMBDA_MEMORY_SIZE = 128  # MB
API_HANDLER_LAMBDA_TIMEOUT = 10  # seconds
POWERTOOLS_SERVICE_NAME = 'POWERTOOLS_SERVICE_NAME'
SERVICE_NAME = 'Orders'
METRICS_NAMESPACE = 'orders_kpi'
METRICS_DIMENSION_KEY = 'service'
POWERTOOLS_TRACE_DISABLED = 'POWERTOOLS_TRACE_DISABLED'
POWER_TOOLS_LOG_LEVEL = 'LOG_LEVEL'
BUILD_FOLDER = '.build/lambdas/'
COMMON_LAYER_BUILD_FOLDER = '.build/common_layer'
ENVIRONMENT = 'dev'
CONFIGURATION_NAME = 'my_conf'
CONFIGURATION_MAX_AGE_MINUTES = '5'  # time to store app config conf in the cache before refetching it
