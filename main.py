from concrete_factory import ConcreteFactory


def main():
    concrete_factory = ConcreteFactory()
    equipment = concrete_factory.create_equipment('backpack')

    for o in (i for i in dir(equipment) if not i.startswith('__')):
        print(
            '\033[1m{:15s}\033[0m {}'.format(o, equipment.__getattribute__(o))
        )


if __name__ == '__main__':
    main()
