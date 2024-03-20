import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    /**
    1. 수업 강의 시간 정보가 들어있는 객체 배열 생성
     2. 각 학생의 비어있는시간을 입력받으면서 반복문을 통해 수강 가능한 강의 검사
     3. 가능하면 시간 증가


     1. 결과 배열의 값을 총 강의 개수로 초기화
     2. 학생들 배열을 돌리면서 해당 강의가 가능한지 검사
     3. 불가능하면 강의 개수를 1 감소하고 continue
     */

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        // 강의 객체 생성
        int totalLecture = Integer.parseInt(br.readLine());
        Lecture[] lectures = new Lecture[totalLecture];
        for(int idx = 0; idx < totalLecture; idx++){
            st = new StringTokenizer(br.readLine());
            lectures[idx] = new Lecture(st);
        }
        //학생 객체 생성
        int totalStudent = Integer.parseInt(br.readLine());
        Student[] students = new Student[totalStudent];
        for(int idx = 0; idx < totalStudent; idx++){
            st = new StringTokenizer(br.readLine());
            students[idx] = new Student(st);
        }

        int[] lecResult = new int[totalStudent];
        Arrays.fill(lecResult,totalLecture);
        // 검사
        for(int student = 0; student < totalStudent; student++){
            for(int lecture = 0; lecture < totalLecture; lecture++){
                for(int time : lectures[lecture].timeTable) {
                    if(!students[student].timeTable.contains(time)){
                        lecResult[student]-=1;
                        break;
                    }
                }
            }
        }
        for (int lec : lecResult) {
            System.out.println(lec);
        }
    }
    static class Lecture{
        ArrayList<Integer> timeTable = new ArrayList<>();
        public Lecture(StringTokenizer st){
            int times = Integer.parseInt(st.nextToken());

            for(int idx = 0; idx < times; idx++){
                int time = Integer.parseInt(st.nextToken());
                timeTable.add(time);
            }
        }
    }
    static class Student{
        ArrayList<Integer> timeTable = new ArrayList<>();

        public Student(StringTokenizer st){
            int times = Integer.parseInt(st.nextToken());

            for(int idx = 0; idx < times; idx++){
                int time = Integer.parseInt(st.nextToken());
                timeTable.add(time);
            }
        }
    }
}