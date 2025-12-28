from src.final_response.response import FinalFormResponse


def print_manual_fields(conf, title):
    print("-----", title, "-----")
    for key in conf.__annotations__.keys():
        if hasattr(conf, key):
            try:
                value = getattr(conf, key).value
            except Exception as e:
                e = '1'
                value = getattr(conf, key)
            print(key, ":", value)
        else:
            print(key, ": Not Found")
    print("-------------------------")


def print_all(response: FinalFormResponse):
    print("IsRendered:", response.is_rendered)
    ##
    print_manual_fields(response.personal_information_response, "Personal Information")

    ##
    print("Employment Information")
    for idx, conf in enumerate(response.employment_information_response.manual_response):
        print_manual_fields(conf, f"Manual Entry {idx + 1}")
    for idx, conf in enumerate(response.employment_information_response.uploaded_response):
        print_manual_fields(conf, f"Uploaded Entry {idx + 1}")

    ##
    print("Tuition Credits Information", response.tuition_credits_information_response)


    if response.tuition_credits_information_response.manual_response is not None:
        print_manual_fields(response.tuition_credits_information_response.manual_response, "Manual")

    if response.tuition_credits_information_response.uploaded_response is not None:
        print_manual_fields(response.tuition_credits_information_response.uploaded_response, "Uploaded")


    ##
    print("Additional Income Information")
    for idx, conf in enumerate(response.additional_income_information_response.uploaded_response):
        print_manual_fields(conf, f"Uploaded Entry {idx + 1}")

    ##
    print("Rental Information", response.rental_information_response)
    for idx, conf in enumerate(response.rental_information_response.manual_response):
        print_manual_fields(conf, f"Manual Entry {idx + 1}")





