from src.final_response.response import FinalFormResponse


def convert_to_dict(response: FinalFormResponse):


    def get_all_from_list(response_list, index_starter=0):
        return {
            f"{index_starter + i}": response_list[i].get_all() for i in range(len(response_list))
        }
    d = {
        'personal_information': response.personal_information_response.get_all(),
        'employment_information': get_all_from_list(response.employment_information_response.manual_response)
    }
