import os

# Path to the directory containing the APK files to test
apk_dir = "/Users/ppunnun/Documents/GitHub/FlowDroid/apk"

# Path to the output directory for the leak reports
output_dir = "/Users/ppunnun/Documents/GitHub/FlowDroid/LeakReports"

# Name of the specific APK file to start processing from
specific_apk_name = "ai.meteum.apk"

# Get a list of all APK files in the directory that come after the specific APK file
apk_list = [f for f in os.listdir(apk_dir) if f.endswith(".apk") and f > specific_apk_name]

# Sort the list alphabetically
apk_list.sort()

# Insert the specific APK file at the beginning of the list
apk_list.insert(0, specific_apk_name)

apk_count = 0

# Loop over all APK files in the directory
for apk_file in apk_list:

    # Increment the counter variable
    apk_count += 1

    # Construct the path to the APK file and the output file
    apk_path = os.path.join(apk_dir, apk_file)
    report_file = os.path.join(output_dir, os.path.splitext(apk_file)[0] + ".txt")

    # Run FlowDroid with the -sink-precise option and save the output to a file
    cmd = f"java -jar soot-infoflow-cmd/target/soot-infoflow-cmd-jar-with-dependencies.jar soot.jimple.infoflow.android.TestApps.Test -a {apk_path} -p /Users/ppunnun/Library/Android/sdk/platforms/android-33/android.jar -s /Users/ppunnun/Documents/GitHub/FlowDroid/soot-infoflow-android/SourcesAndSinks.txt -sink-precise -o {report_file}"
    os.system(cmd)

    # Print the current APK count and file name
    print(f"Processed APK {apk_count}: {apk_file}", "\n")
