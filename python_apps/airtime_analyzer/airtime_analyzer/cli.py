"""
Main CLI entrypoint for the libretime-analyzer app.
"""

import argparse
import os

import airtime_analyzer.airtime_analyzer as aa

VERSION = "1.0"
LIBRETIME_CONF_DIR = os.getenv("LIBRETIME_CONF_DIR", "/etc/airtime")
DEFAULT_RMQ_CONFIG_PATH = os.path.join(LIBRETIME_CONF_DIR, "airtime.conf")
DEFAULT_HTTP_RETRY_PATH = "/tmp/airtime_analyzer_http_retries"


def main():
    """Entry-point for this application"""
    print("LibreTime Analyzer {}".format(VERSION))
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug", help="log full debugging output", action="store_true"
    )
    parser.add_argument(
        "--rmq-config-file",
        help="specify a configuration file with RabbitMQ settings (default is %s)"
        % DEFAULT_RMQ_CONFIG_PATH,
    )
    parser.add_argument(
        "--http-retry-queue-file",
        help="specify where incompleted HTTP requests will be serialized (default is %s)"
        % DEFAULT_HTTP_RETRY_PATH,
    )
    args = parser.parse_args()

    # Default config file path
    rmq_config_path = DEFAULT_RMQ_CONFIG_PATH
    http_retry_queue_path = DEFAULT_HTTP_RETRY_PATH
    if args.rmq_config_file:
        rmq_config_path = args.rmq_config_file
    if args.http_retry_queue_file:
        http_retry_queue_path = args.http_retry_queue_file

    aa.AirtimeAnalyzerServer(
        rmq_config_path=rmq_config_path,
        http_retry_queue_path=http_retry_queue_path,
        debug=args.debug,
    )


if __name__ == "__main__":
    main()
