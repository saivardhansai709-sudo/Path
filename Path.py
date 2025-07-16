def main():
    parser = argparse.ArgumentParser(description="Web Application Vulnerability Scanner")
    parser.add_argument("url", help="Target URL (with http:// or https://)")
    parser.add_argument("-t", "--txt", help="Text report output (default: vuln_report.txt)", default="vuln_report.txt")
    parser.add_argument("-p", "--pdf", help="PDF report output (default: vuln_report.pdf)", default="vuln_report.pdf")
    args = parser.parse_args()

    if not args.url.startswith("http"):
        print("[-] Please include http:// or https:// in the URL.")
        return

    scan_xss_sql_csrf(args.url)
    save_report(args.url, args.txt)
    save_pdf_report(args.url, results, args.pdf)
