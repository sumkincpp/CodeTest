// http://parroty00.wordpress.com/2013/07/18/golang-tcp-server-example/
package main
 
import (
  "io"
  "log"
  "net"
  "bytes"
  "bufio"
  "strings"
  "time"
)
 
type JobInterface interface {
  run() string
}
type Job        struct { param string }
type SmallJob   struct { Job }
type LargeJob   struct { Job }
type InvalidJob struct { Job }
 
func (job SmallJob) run() string {
  time.Sleep(1 * time.Second)
  return "Completed in 1 second with param = " + job.param
}
 
func (job LargeJob) run() string {
  time.Sleep(5 * time.Second)
  return "Completed in 5 second with param = " + job.param
}
 
func (job InvalidJob) run() string {
  return "Invalid command is specified"
}
 
func job_runner(job JobInterface, out chan string) {
  out <- job.run() + "\n"
}
 
func job_factory(input string) JobInterface {
  array := strings.Split(input, " ")
  if len(array) >= 2 {
    command := array[0]
    param   := array[1]
 
    if command == "SMALL" {
      return SmallJob{Job{param}}
    } else if command == "LARGE" {
      return LargeJob{Job{param}}
    }
  }
  return InvalidJob{Job{""}}
}
 
func request_handler(conn net.Conn, out chan string) {
  defer close(out)
 
  for {
    line, err := bufio.NewReader(conn).ReadBytes('\n')
    if err != nil { return }
 
    job := job_factory(strings.TrimRight(string(line), "\n"))
    go job_runner(job, out)
  }
}
 
func send_data(conn net.Conn, in <-chan string) {
  defer conn.Close()
 
  for {
    message := <- in
    log.Print(message)
    io.Copy(conn, bytes.NewBufferString(message))
  }
}
 
func main() {
  psock, err := net.Listen("tcp", ":5000")
  if err != nil { return }
 
  for {
    conn, err := psock.Accept()
    if err != nil { return }
 
    channel := make(chan string)
    go request_handler(conn, channel)
    go send_data(conn, channel)
  }
}
