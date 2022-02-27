def rgx_compare_single(rgx, str): # compare one to one
    if len(rgx) == 0:
        return True
    if rgx == str:
        return True
    if rgx == ".":
        return True
    return False


def rgx_compare_recur(regex_inp, str_inp): # recursive comparison
    if len(regex_inp) > len(str_inp):
        return False # regex cant be longer for now
    if len(regex_inp) == 0: # stop if reg is empty
        return True
    match = rgx_compare_single(regex_inp[0], str_inp[0])
    if match:
        if len(regex_inp) > 1:
            return rgx_compare_recur(regex_inp[1:], str_inp[1:])
    return match

class RegexEngine:

    def __init__(self,regex_inp, str_inp):
        self.outcome = False
        self.regex_inp, self.str_inp = regex_inp, str_inp
        if len(self.regex_inp) == 0:  # stop if reg is empty
            self.outcome = True


    def stage_2(self,regex_inp,str_inp):
        outcome = self.rgx_compare_recur(regex_inp, str_inp)
        if outcome:
            self.outcome = outcome

    def stage_3(self,regex_inp,str_inp):
        for length in range(len(str_inp)):
            current_outcome = self.rgx_compare_recur(regex_inp, str_inp[length:])
            if current_outcome:
                self.outcome = current_outcome

    def stage_4(self):
        pass


    def rgx_compare_single(self, rgx, strng): # compare one to one
        if len(rgx) == 0:
            return True
        if rgx == strng:
            return True
        if rgx == ".":
            return True
        return False

    def one_ques_star_plus_case(self, symbol, regex_inp, str_inp):
        index_for_symbol = regex_inp.find(symbol)
        regex_without = regex_inp[:(index_for_symbol - 1)] + regex_inp[index_for_symbol + 1:]
        outcome_without =  self.rgx_compare_recur(regex_without, str_inp)
        if outcome_without and (symbol != "+"):
            return outcome_without
        if symbol == "*":
            for repeat in range(1,(len(str_inp)-len(regex_without))+2):
                regex_with = regex_inp[:index_for_symbol - 1] + repeat * regex_inp[index_for_symbol - 1] + regex_inp[index_for_symbol + 1:]
                outcome_repeat = self.rgx_compare_recur(regex_with, str_inp)
                if outcome_repeat:
                    return outcome_repeat
        elif symbol == "+":
            for repeat in range(1, (len(str_inp)-len(regex_without))+3):
                regex_with = regex_inp[:index_for_symbol - 1] + repeat * regex_inp[index_for_symbol - 1] + regex_inp[index_for_symbol + 1:]
                outcome_with = self.rgx_compare_recur(regex_with, str_inp)
                if outcome_with:
                    return outcome_with
        else:
            regex_with = regex_inp[:index_for_symbol] + regex_inp[index_for_symbol + 1:]
            outcome_with = self.rgx_compare_recur(regex_with, str_inp)
            return outcome_with


    def rgx_compare_recur(self, regex_inp, str_inp):  # recursive comparison
        if len(regex_inp) == 0:  # stop if reg is empty
            return True
        slash = False ######################## here
        if regex_inp[0] == "\\": ######################## here
            regex_inp = regex_inp[1:] ######################## here
            slash = True ######################## here
        if ("+" in regex_inp) and not slash and (regex_inp[regex_inp.find("+")-1] != "\\"): ######################## here
            return self.one_ques_star_plus_case("+", regex_inp, str_inp)
        if "*" in regex_inp:
            return self.one_ques_star_plus_case("*", regex_inp, str_inp)
        if len(regex_inp) > len(str_inp):
            if regex_inp[-1] == "$":
                return self.rgx_compare_recur(regex_inp[:-1], str_inp)
            if "?" in regex_inp and (regex_inp[regex_inp.find("?")-1] != "\\"):
                return self.one_ques_star_plus_case("?", regex_inp, str_inp)
            return False  # regex cant be longer for now
        match = self.rgx_compare_single(regex_inp[0], str_inp[0])
        if match:
            if len(regex_inp) > 1:
                return self.rgx_compare_recur(regex_inp[1:], str_inp[1:])
        return match

def regex_engine(regex_inp, str_inp):
    rre = RegexEngine(regex_inp, str_inp)
    if rre.outcome is False:
        first_charachter = regex_inp[0]
        if first_charachter == "^":
            rre.stage_2(regex_inp[1:],str_inp)
            rre.outcome
        else:
            rre.stage_3(regex_inp,str_inp)
    return rre.outcome

def main():
    regex_inp, str_inp = input().split("|")
    print(regex_engine(regex_inp, str_inp))



if __name__ == '__main__':
    main()
    # This project was a multi-step project, here are some historic relics of its construction:

    # # run according to stage
    # if stage == 1:
    #     outcome = rgx_compare_single(regex_inp, str_inp)
    # if stage == 2:
    #     outcome = rgx_compare_recur(regex_inp, str_inp)
    # if stage == 3:
    #     outcome = False
    #     if len(regex_inp) == 0:  # stop if reg is empty
    #         outcome = True
    #     for length in range(len(str_inp)):
    #         current_outcome = rgx_compare_recur(regex_inp, str_inp[length:])
    #         if current_outcome:
    #             outcome = current_outcome
    #     print(outcome)
    #
    # if stage == 4: # created a class
    #     rre = RegexEngine(regex_inp, str_inp)
    #     if rre.outcome is False:
    #         first_charachter = regex_inp[0]
    #         if first_charachter == "^":
    #             rre.stage_2(regex_inp[1:],str_inp)
    #             rre.outcome
    #         else:
    #             rre.stage_3(regex_inp,str_inp)
    #     print(rre.outcome)







