import capsolver
from urllib.parse import urlparse

# Change this information
PARSED_PROXY = "http://username:password@host:port"

capsolver.api_key = "Your pay per usage key"

def solve_hcaptcha_nfe():
    solution = capsolver.solve({
        "type": "HCaptchaTask",
        "websiteURL": "https://www.restituicao.receita.fazenda.gov.br",
        "websiteKey": "1e7b8462-5e38-4418-9998-74210d909134",
        "proxy": PARSED_PROXY
    })
    return solution

def main():
    
    print("Solving nfe captcha")
    solution = solve_hcaptcha_nfe()
    
    token = solution["gRecaptchaResponse"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
