import capsolver
from urllib.parse import urlparse

# Change this information
PARSED_PROXY = "http://username:password@host:port"

capsolver.api_key = "Your pay per usage key"

def solve_hcaptcha_nfe():
    solution = capsolver.solve({
        "type": "HCaptchaTask",
        "websiteURL": "https://servicos.receita.fazenda.gov.br",
        "websiteKey": "53be2ee7-5efc-494e-a3ba-c9258649c070",
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
