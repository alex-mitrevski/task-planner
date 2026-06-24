import yaml
from task_planner.lama_interface import LAMAInterface

if __name__ == '__main__':
    with open('../config/planner_config.yaml', 'r') as config_file:
        planner_config = yaml.safe_load(config_file)
        domain_file = planner_config['domain_file']
        planner_cmd = planner_config['planner_cmd']
        plan_file_path = planner_config['plan_file_path']

        state_fluents = [('empty_gripper', [('bot', 'myrobot')], 'true'),
                         ('robot_at', [('bot', 'myrobot')], 'PICKUP_LOCATION'),
                         ('load_at', [('load', 'custom_load')], 'PICKUP_LOCATION')]

        floor_fluents = [('elevator_at', [('elevator', 'automatic_elevator'), ('loc', 'ELEVATOR0')], 'true'),
                         ('elevator_at', [('elevator', 'automatic_elevator'), ('loc', 'ELEVATOR1')], 'true'),
                         ('elevator_at', [('elevator', 'automatic_elevator'), ('loc', 'ELEVATOR2')], 'true'),
                         ('robot_floor', [('bot', 'myrobot')], 'floor0'),
                         ('load_floor', [('load', 'custom_load')], 'floor0'),
                         ('elevator_floor', [('elevator', 'automatic_elevator')], 'unknown'),
                         ('destination_floor', [('elevator', 'automatic_elevator')], 'unknown'),
                         ('location_floor', [('loc', 'PICKUP_LOCATION')], 'floor0'),
                         ('location_floor', [('loc', 'DELIVERY_LOCATION')], 'floor0'),
                         ('location_floor', [('loc', 'ELEVATOR0')], 'floor0'),
                         ('location_floor', [('loc', 'ELEVATOR2')], 'floor2')]

        planner_interface = LAMAInterface('test_kb', domain_file, planner_cmd, plan_file_path, debug=True)
        planner_interface.kb_interface.insert_fluents(state_fluents)
        planner_interface.kb_interface.insert_fluents(floor_fluents)

        load_id = 'custom_load'
        delivery_pose_id = 'DELIVERY_LOCATION'

        task_goals = [('load_at', [('load', load_id)], delivery_pose_id),
                      ('empty_gripper', [('bot', 'myrobot')], 'true')]
        plan_found, plan = planner_interface.plan('myrobot', task_goals)

        planner_interface.kb_interface.remove_fluents(state_fluents)
        planner_interface.kb_interface.remove_fluents(floor_fluents)

        planner_interface.kb_interface.db_client.drop_database('test_kb')