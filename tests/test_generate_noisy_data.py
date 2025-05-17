from kalman import generate_noisy_data


def test_generate_noisy_data_shape():
    dT = 1
    A = [
        [1, 0, dT, 0],
        [0, 1, 0, dT],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    x = [0, 0, 1, 1]
    vals = 5
    sigma = 0.1
    data = generate_noisy_data(A, x, vals, sigma)
    assert len(data) == vals
    assert all(len(row) == 2 for row in data)

