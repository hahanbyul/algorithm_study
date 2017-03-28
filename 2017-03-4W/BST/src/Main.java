import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Main {
//	public static Queue<Integer> get_
	
	public static void print_queue(Queue<Integer> q) {
		if (q.isEmpty()) return;
		for (int i : q) {
			System.out.print(i + " ");
		}
		System.out.println();
	}
	
	public static Map<Integer, Integer> get_less_keys(RedBlackBST<Integer, Integer> st, int num) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int less_num : st.keys(0, num-1)) {
			map.put(st.get(less_num), less_num);
		}
		return map;
	}

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int C = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < C; i++) {
			RedBlackBST<Integer, Integer> st_of_p = new RedBlackBST<Integer, Integer>();
			RedBlackBST<Integer, Integer> st_of_q = new RedBlackBST<Integer, Integer>();

			int N = Integer.parseInt(sc.nextLine());
			for (int j = 0; j < N; j++) {
				String[] p_and_q = sc.nextLine().split(" ");

				int p = Integer.parseInt(p_and_q[0]);
				int q = Integer.parseInt(p_and_q[1]);

				st_of_p.put(p, j);
				st_of_q.put(q, j);
				
				Map<Integer, Integer> map_of_p = get_less_keys(st_of_p, p-1);
				Map<Integer, Integer> map_of_q = get_less_keys(st_of_q, q-1);
				
				Set<Integer> set_of_p = new HashSet<Integer>(map_of_p.keySet());
				Set<Integer> set_of_q = new HashSet<Integer>(map_of_q.keySet());
				set_of_p.retainAll(set_of_q);

				for (int s : set_of_p) {
					int p_to_remove = map_of_p.get(s);
					int q_to_remove = map_of_q.get(s);

					st_of_p.delete(p_to_remove);
					st_of_q.delete(q_to_remove);

					System.out.printf("removed ID %d: (%d, %d)\n", s, p_to_remove, q_to_remove);

				}

				System.out.printf("# of IDs: %d\n", st_of_p.size());

			}

//			for (int s : st_of_p.keys())
//				System.out.println(s + " " + st_of_p.get(s));
//
//			for (int s : st_of_q.keys())
//				System.out.println(s + " " + st_of_q.get(s));
        }
	}
}
