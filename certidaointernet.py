import capsolver
from urllib.parse import urlparse

# Change this information
PARSED_PROXY = "http://username:password@host:port"

capsolver.api_key = "Your pay per usage key"

def solve_hcaptcha_nfe():
    solution = capsolver.solve({
        "type": "HCaptchaTask",
        "websiteURL": "https://solucoes.receita.fazenda.gov.br",
        "websiteKey": "4a65992d-58fc-4812-8b87-789f7e7c4c4b",
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
