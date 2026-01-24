import numpy as np

np.random.seed(42)

student_ids = np.arange(1, 100001)
scores = np.random.randint(0, 101, size=100000)

data = np.column_stack((student_ids, scores))

np.savetxt(
    "data/exam_scores.csv",
    data,
    delimiter=",",
    header="student_id,score",
    comments="",
    fmt="%d",
)

print("We are successful")
print("Total students: ", scores.size)
print("Average score: ", np.mean(scores))
print("Highest score:", np.max(scores))
print("lowest score", np.min(scores))
print("Starndard deviation", np.std(scores))