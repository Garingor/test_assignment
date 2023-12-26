def print_num_gt(y: int):
    def print_num_gt_decorator(function):
        def wrapper(x: int):
            if x > y:
                result = function(x)
            else:
                raise Exception('error')
            return result

        return wrapper

    return print_num_gt_decorator


@print_num_gt(3)
def print_num(x: int):
    print(x)


if __name__ == '__main__':
    print_num(5)
    #print_num(1)
