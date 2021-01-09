def handle_black(func):
    def handle(*args, **kwargs):
        base_page = args[0]
        # print("args[0]=%s" % base_page)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # print("1111")
            for locator in base_page.black_list:
                print(locator)
                els = base_page.driver.find_elements(*locator)
                print(len(els))
                if len(els) > 0:
                    els[0].click()
                    return func(*args, **kwargs)
            raise e
    return handle
