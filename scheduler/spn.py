from scheduler.abstract_scheduler import AbstractScheduler

class SPNScheduler(AbstractScheduler):
    def do_schedule(self):
        # 모든 코어를 순회하며 빈 코어 탐색
        for core in self.cores:
            
            # 코어가 비어있고 레디 큐에 대기 중인 프로세스가 있는지 확인
            if core.is_idle() and self.ready_queue:
                
                # 레디 큐 안의 모든 프로세스들 중 실행 시간(BT)이 가장 짧은 프로세스 탐색
                best_process = min(
                    self.ready_queue,
                    key=lambda p: (p.bt, p.at, p.p_id)
                )
                
                # 가장 짧은 작업을 가진 프로세스를 레디 큐에서 제거
                self.ready_queue.remove(best_process)
                
                # 빈 코어에 해당 프로세스를 할당
                core.allocate(best_process)
