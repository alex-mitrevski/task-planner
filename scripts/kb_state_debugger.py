#!/usr/bin/env python3
import os
import time
from task_planner.knowledge_base_interface import KnowledgeBaseInterface


def get_param_values(instance):
    values = [v.value for v in instance.params]
    return values


if __name__ == '__main__':
    kb_interface = KnowledgeBaseInterface('test_kb')
    try:
        while True:
            fluents = kb_interface.get_fluent_names()
            for fluent in fluents:
                fluent_instances = kb_interface.get_fluent_assertions(fluent)
                if fluent_instances:
                    print(fluent)
                    print('--------------------')
                    for instance in fluent_instances:
                        param_values = get_param_values(instance)
                        instance_str = ''
                        for v in param_values[0:-1]:
                            instance_str += '{0}, '.format(v)
                        instance_str += '{0}'.format(param_values[-1])

                        if instance.value != 'true' and instance.value != 'false':
                            print(f'{fluent}: ( {instance_str} {instance.value} )')
                        else:
                            print(f'{fluent}: ( {instance_str} )')
                    print()
            time.sleep(1.)
            os.system('clear')
    except (KeyboardInterrupt, SystemExit):
        print('Ending knowledge base visualiser')
