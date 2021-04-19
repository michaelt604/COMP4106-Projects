import logging
import numpy
import os
import sys
import traceback


Q_VALUE_THRESHOLD = 1e-2

Q_VALUE_MARKS = 5
POLICY_MARKS = 5
CASE_TOTAL_MARKS = 10


# Compare 
def compare_q_values(agent, q_value_tests_values):
  correct_q_values = 0
  for i in range(q_value_tests_values.shape[0]):
    curr_q_value = agent.qvalue(q_value_tests_values[i, 0], q_value_tests_values[i, 1])
    q_value_diff = abs(curr_q_value - float(q_value_tests_values[i, 2]))

    if q_value_diff < Q_VALUE_THRESHOLD:
      correct_q_values = correct_q_values + 1
    else:
      logging.warning("Student's calculated q-value differs by: " + str(q_value_diff) + ".")
  
  return Q_VALUE_MARKS * correct_q_values / q_value_tests_values.shape[0]


def compare_policies(agent, policy_tests_values):
  correct_policies = 0
  for i in range(policy_tests_values.shape[0]):
    curr_policy = agent.policy(policy_tests_values[i, 0])
    policy_diff = (curr_policy == policy_tests_values[i, 1])

    if policy_diff :
      correct_policies = correct_policies + 1
    else:
      logging.warning("Student's calculated policy was: " + curr_policy + ". Expected policy: " + policy_tests_values[i, 1] + ".")
  
  return POLICY_MARKS * correct_policies / policy_tests_values.shape[0]


if __name__ == "__main__":
  # Assume we have all examples in same folder  
  test_case_path = sys.argv[1]
  student_code_path = sys.argv[2]
  test_case_folders = os.listdir(test_case_path)

  sys.path.append(student_code_path)
  from assignment3 import *  

  achieved_marks = []
  
  for i in range(len(test_case_folders)):
    print("===== " + test_case_folders[i] + " =====")
    curr_achieved_marks = 0

    trajectory_filepath = os.path.join(test_case_path, test_case_folders[i], "trajectory.csv")

    q_value_tests_filepath = os.path.join(test_case_path, test_case_folders[i], "q_value_tests.csv")
    policy_tests_filepath = os.path.join(test_case_path, test_case_folders[i], "policy_tests.csv")

    q_value_tests_values = numpy.loadtxt(q_value_tests_filepath, dtype="str", delimiter=",").reshape(-1, 3)
    policy_tests_values = numpy.loadtxt(policy_tests_filepath, dtype="str", delimiter=",").reshape(-1, 2)

    try:
      agent = td_qlearning(trajectory_filepath)
    except Exception as e:
      logging.warning("Exception during initialization.")
      logging.warning(e)
      logging.warning(traceback.format_exc())

    try:
      q_values_achieved_marks = compare_q_values(agent, q_value_tests_values)
      curr_achieved_marks = curr_achieved_marks + q_values_achieved_marks
    except Exception as e:
      logging.warning("Exception during computation of q-values.")
      logging.warning(e)
      logging.warning(traceback.format_exc())

    try:
      policies_achieved_marks = compare_policies(agent, policy_tests_values)
      curr_achieved_marks = curr_achieved_marks + policies_achieved_marks
    except Exception as e:
      logging.warning("Exception during computation of policies.")
      logging.warning(e)
      logging.warning(traceback.format_exc())
  
    achieved_marks.append(curr_achieved_marks)

  print("Achieved marks for each test case (each out of " + str(CASE_TOTAL_MARKS) + "): " + str(achieved_marks))
  total_achieved_marks = sum(achieved_marks) / (CASE_TOTAL_MARKS * len(achieved_marks))
  print("Percentage acheived marks for all test cases: " + str(100 * total_achieved_marks) + "%.")