def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def abbr(abbreviation):
        "Create an <abbr/>"
        try:
            title=env.variables.abbreviation[abbreviation]
            return "<abbr title=\"{title}\">{abbreviation}</abbr>".format(title=title, abbreviation=abbreviation)
        except:
            return abbreviation
    