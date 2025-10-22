def deduplicate_list(input_list):
    """去重功能（基于之前练习）"""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    # 示例用法
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {sample_list}")
    print(f"Deduplicated: {deduplicate_list(sample_list)}")