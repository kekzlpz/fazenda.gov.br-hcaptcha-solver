import capsolver
from urllib.parse import urlparse

# Change this information
PARSED_PROXY = "http://username:password@host:port"

capsolver.api_key = "Your pay per usage key"

def solve_hcaptcha_nfe():
    solution = capsolver.solve({
        "type": "HCaptchaTask",
        "websiteURL": "https://sinac.cav.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgdasd2018.app/Captcha",
        "websiteKey": "38604819-bb1e-4105-b3bf-49c1ffdf9475",
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
