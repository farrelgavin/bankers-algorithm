def bankers_algorithm():

# jumlah proses dan resource
    num_processes=5
    num_resources=3

# resource yang masih tersedia
    available=[3, 3, 2]

# resource yang sudah dipegang tiap proses
    allocation=[
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2],  # P4
    ]

# kebutuhan maksimal tiap proses
    max_need=[
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3],  # P4
    ]


# hitung need (max - allocation)
    need=[]
    for i in range(num_processes):
        row=[]
        for j in range(num_resources):
            row.append(max_need[i][j] - allocation[i][j])
        need.append(row)
        
    print("BANKER'S ALGORITHM")
    print(f"\n{'Jumlah Proses'}: {num_processes}")
    print(f"{'Jumlah Resource'}: {num_resources}")
    print(f"{'Available'}: {available}  (A, B, C)")

    print("\nMatriks Allocation")
    print(f"{'Proses'} {'A'} {'B'} {'C'}")
    for i in range(num_processes):
        print(f"P{i} {allocation[i][0]} {allocation[i][1]} {allocation[i][2]}")

    print("\nMatriks Max Need")
    print(f"{'Proses'} {'A'} {'B'} {'C'}")
    for i in range(num_processes):
        print(f"P{i} {max_need[i][0]} {max_need[i][1]} {max_need[i][2]}")

    print("\nMatriks Need")
    print(f"{'Proses'} {'A'} {'B'} {'C'}")
    for i in range(num_processes):
        print(f"P{i} {need[i][0]} {need[i][1]} {need[i][2]}")

# jalankan safety algorithm untuk cari safe sequence
    print("\nSafety Algorithm\n")

    work=available[:]
    finish=[False] * num_processes
    safe_sequence=[]
    step=1

    while len(safe_sequence) < num_processes:
        found=False
        for i in range(num_processes):
            if not finish[i]:

                # cek satu per satu apakah need <= work
                can_execute=True
                for j in range(num_resources):
                    if need[i][j] > work[j]:
                        can_execute=False
                        break

                if can_execute:
                    print(f"Step {step}: P{i} bisa dieksekusi")
                    print(f"Need P{i}: {need[i]}")
                    print(f"Work sekarang: {work}")

                    # setelah selesai, kembalikan resource ke work
                    for j in range(num_resources):
                        work[j]=work[j] + allocation[i][j]
                    print(f"Work setelah P{i} release: {work}\n")

                    finish[i]=True
                    safe_sequence.append(f"P{i}")
                    found=True
                    step+=1
                    break

        if not found:
            break

# tampilkan hasil akhir
    if len(safe_sequence)==num_processes:
        print("SAFE STATE")
        print(f"Safe Sequence: {' → '.join(safe_sequence)}")
    else:
        print("UNSAFE STATE - Deadlock terjadi!")

bankers_algorithm()